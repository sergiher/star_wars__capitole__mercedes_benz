import {
  MaterialReactTable,
  type MRT_ColumnDef,
  type MRT_SortingState,
} from "material-react-table";
import { useEffect, useMemo, useState } from "react";
import { Box } from "@mui/material";

import {
  getPeopleDataApi,
  postSortingDataApi,
} from "~/infrastructure/api/dataApi";

type Person = {
  name: string;
  height: string;
  mass: string;
  hair_color: string;
  skin_color: string;
  eye_color: string;
  birth_year: string;
  gender: string;
  homeworld: string;
  films: string[];
  species: string[];
  vehicles: string[];
  starships: string[];
  created: string;
  edited: string;
  url: string;
};

export function Welcome() {
  const [data, setData] = useState<Person[]>([]);
  const [loading, setLoading] = useState(true);
  const [sorting, setSorting] = useState<MRT_SortingState>([]);

  const fetchDataWithSorting = async (sortingState: MRT_SortingState) => {
    setLoading(true);
    try {
      const sortParams = sortingState.map((sort) => ({
        field: sort.id,
        direction: sort.desc ? "desc" : "asc",
      }));

      const response = await postSortingDataApi(sortParams);

      const result = await response.json();
      setData(result);
    } catch (error) {
      console.error("Error fetching sorted data:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchDataWithSorting(sorting);
  }, [sorting]);

  const columns = useMemo<MRT_ColumnDef<Person>[]>(
    () => [
      {
        accessorKey: "name",
        header: "Name",
      },
      {
        accessorKey: "created",
        header: "Created",
      },
    ],
    []
  );

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getPeopleDataApi();
        const json = await response.json();
        setData(json);
      } catch (error) {
        console.error("Failed to fetch data", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <Box p={4}>
      <MaterialReactTable
        columns={columns}
        data={data}
        state={{ isLoading: loading, sorting: sorting }}
        enableSorting
        enableGlobalFilter
        enableStickyHeader
        manualSorting={true}
        onSortingChange={setSorting}
        initialState={{
          pagination: {
            pageSize: 15,
            pageIndex: 0,
          },
        }}
      />
    </Box>
  );
}
