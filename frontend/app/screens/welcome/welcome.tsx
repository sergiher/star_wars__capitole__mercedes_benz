import React, { useRef } from "react";
import {
  MaterialReactTable,
  type MRT_ColumnDef,
  type MRT_SortingState,
} from "material-react-table";
import { useEffect, useMemo, useState } from "react";
import {
  Box,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  Typography,
  type SelectChangeEvent,
} from "@mui/material";

type Person = {
  name: string;
  created: string;
};

type Planet = {
  name: string;
  created: string;
};

import { postSortingDataApi } from "~/infrastructure/api/dataApi";
import { fetchAiInsightApi } from "~/infrastructure/api/aiInsight";
import { showToast } from "~/infrastructure/ui/ToastService";

function getColumns(
  entityType: EntityType,
  loadingAIName: string | null,
  handleAiInsightClick: (type: EntityType, name: string) => void
): MRT_ColumnDef<Person | Planet>[] {
  return [
    {
      accessorKey: "name",
      header: "Name",
      size: 100,
    },
    {
      accessorKey: "created",
      header: "Created",
      size: 100,
    },
    {
      header: "AI Insight",
      id: "ai_insight_button",
      Cell: ({ row }) =>
        loadingAIName === row.original.name ? (
          <span className="loader" />
        ) : (
          <button
            onClick={() => handleAiInsightClick(entityType, row.original.name)}
            className="ai_insight_button"
          >
            Ask AI
          </button>
        ),
      size: 100,
    },
  ];
}

export function Welcome() {
  const peopleInitialized = useRef(false);
  const planetsInitialized = useRef(false);
  const [peopleData, setPeopleData] = useState<Person[]>([]);
  const [planetsData, setPlanetsData] = useState<Planet[]>([]);
  const [loadingPeople, setLoadingPeople] = useState(true);
  const [loadingPlanets, setLoadingPlanets] = useState(true);
  const [loadingAIName, setLoadingAIName] = useState<string | null>(null);
  const [sortingPeople, setSortingPeople] = useState<MRT_SortingState>([]);
  const [sortingPlanets, setSortingPlanets] = useState<MRT_SortingState>([]);
  const [algorithm, setAlgorithm] = useState("");

  async function handleAiInsightClick(entityType: string, name: string) {
    try {
      setLoadingAIName(name);
      const message = await fetchAiInsightApi(entityType, name);
      const formattedMessage = message.substring(1, message.length - 3);
      showToast("info", formattedMessage);
    } catch (error: any) {
      showToast(
        "error",
        JSON.parse(error.message).detail || "Unexpected error"
      );
    } finally {
      setLoadingAIName(null);
    }
  }
  async function fetchSortedData<T>(
    entityType: string,
    sortingState: MRT_SortingState,
    setDataFn: (data: T[]) => void,
    setLoadingFn: (loading: boolean) => void
  ) {
    setLoadingFn(true);
    try {
      const sortParams = sortingState.map((sort) => ({
        field: sort.id,
        direction: sort.desc ? "desc" : "asc",
        algorithm: algorithm,
      }));

      const response = await postSortingDataApi(
        entityType,
        sortParams.length > 0 ? sortParams : undefined
      );
      const result = await response.json();
      setDataFn(result);
    } catch (error) {
      console.error("Error fetching sorted data:", error);
    } finally {
      setLoadingFn(false);
    }
  }

  useEffect(() => {
    if (!peopleInitialized.current) {
      peopleInitialized.current = true;
      return;
    }
    fetchSortedData("people", sortingPeople, setPeopleData, setLoadingPeople);
  }, [sortingPeople]);

  useEffect(() => {
    if (!planetsInitialized.current) {
      planetsInitialized.current = true;
      return;
    }

    fetchSortedData(
      "planets",
      sortingPlanets,
      setPlanetsData,
      setLoadingPlanets
    );
  }, [sortingPlanets]);

  const columns = useMemo<MRT_ColumnDef<Person | Planet>[]>(
    () => [
      {
        accessorKey: "name",
        header: "Name",
        size: 100,
      },
      {
        accessorKey: "created",
        header: "Created",
        size: 100,
      },
      {
        header: "AI Insight",
        id: "ai_insight_button",
        Cell: ({ row }) =>
          loadingAIName === row.original.name ? (
            <span className="loader" />
          ) : (
            <button
              onClick={() => handleAiInsightClick("people", row.original.name)}
              className="ai_insight_button"
            >
              Ask AI
            </button>
          ),
        size: 100,
      },
    ],
    [loadingAIName]
  );

  useEffect(() => {
    fetchSortedData("people", sortingPeople, setPeopleData, setLoadingPeople);
    fetchSortedData(
      "planets",
      sortingPlanets,
      setPlanetsData,
      setLoadingPlanets
    );
  }, []);

  const peopleColumns = useMemo(
    () => getColumns("people", loadingAIName, handleAiInsightClick),
    [loadingAIName]
  );

  const planetColumns = useMemo(
    () => getColumns("planets", loadingAIName, handleAiInsightClick),
    [loadingAIName]
  );

  return (
    <Box textAlign="center">
      <FormControl sx={{ mb: 3, minWidth: 200, margin: 3 }}>
        <InputLabel id="algorithm-select-label">Sorting Algorithm</InputLabel>
        <Select
          labelId="algorithm-select-label"
          id="algorithm-select"
          value={algorithm}
          label="Sorting Algorithm"
          onChange={(event: SelectChangeEvent) => {
            setAlgorithm(event.target.value);
          }}
        >
          <MenuItem value="power_sort">Power Sort</MenuItem>
          <MenuItem value="bubble_sort">Bubble Sort</MenuItem>
          <MenuItem value="selection_sort">Selection Sort</MenuItem>
        </Select>
      </FormControl>

      <Box
        display="flex"
        flexWrap="wrap"
        gap={4}
        justifyContent="space-between"
        padding={5}
      >
        <Box flex={1} minWidth="500px">
          <Typography variant="h6" gutterBottom>
            People
          </Typography>
          <MaterialReactTable
            columns={peopleColumns}
            data={peopleData}
            state={{ isLoading: loadingPeople, sorting: sortingPeople }}
            enableSorting
            enableGlobalFilter
            enableStickyHeader
            manualSorting={true}
            onSortingChange={setSortingPeople}
            initialState={{
              pagination: {
                pageSize: 15,
                pageIndex: 0,
              },
            }}
          />
        </Box>

        <Box flex={1} minWidth="500px">
          <Typography variant="h6" gutterBottom>
            Planets
          </Typography>
          <MaterialReactTable
            columns={planetColumns}
            data={planetsData}
            state={{ isLoading: loadingPlanets, sorting: sortingPlanets }}
            enableSorting
            enableGlobalFilter
            enableStickyHeader
            manualSorting={true}
            onSortingChange={setSortingPlanets}
            initialState={{
              pagination: {
                pageSize: 15,
                pageIndex: 0,
              },
            }}
          />
        </Box>
      </Box>
    </Box>
  );
}
