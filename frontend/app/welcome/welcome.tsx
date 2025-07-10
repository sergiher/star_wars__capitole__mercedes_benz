// @ts-ignore
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

import { postSortingDataApi } from "~/infrastructure/api/dataApi";

type Person = {
  name: string;
  created: string;
};

type Planet = {
  name: string;
  created: string;
};

export function Welcome() {
  const peopleInitialized = useRef(false);
  const planetsInitialized = useRef(false);
  const [peopleData, setPeopleData] = useState<Person[]>([]);
  const [planetsData, setPlanetsData] = useState<Planet[]>([]);
  const [loadingPeople, setLoadingPeople] = useState(true);
  const [loadingPlanets, setLoadingPlanets] = useState(true);
  const [sortingPeople, setSortingPeople] = useState<MRT_SortingState>([]);
  const [sortingPlanets, setSortingPlanets] = useState<MRT_SortingState>([]);
  const [algorithm, setAlgorithm] = useState("");

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
    ],
    []
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
            columns={columns}
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
            columns={columns}
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
