import { MaterialReactTable, type MRT_ColumnDef } from "material-react-table";
import { useEffect, useMemo, useState } from "react";
import { Box } from "@mui/material";

import { getPeopleDataApi } from "~/infrastructure/api/dataApi";

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
        state={{ isLoading: loading }}
        enableSorting
        enableGlobalFilter
        enableStickyHeader
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
