// frontend/app/welcome/welcome.tsx
import { MaterialReactTable, type MRT_ColumnDef } from "material-react-table";
import { useMemo } from "react";
import { Box } from "@mui/material";

type Person = {
  name: string;
  planet: string;
};

const mockData: Person[] = [
  { name: "Luke Skywalker", planet: "Tatooine" },
  { name: "Luke Skywalker", planet: "Tatooine" },
  { name: "Luke Skywalker", planet: "Tatooine" },
  { name: "Luke Skywalker", planet: "Tatooine" },
  { name: "Luke Skywalker", planet: "Tatooine" },
  { name: "Luke Skywalker", planet: "Tatooine" },
  { name: "Robert", planet: "Bomsky" },
  { name: "Robert", planet: "Bomsky" },
  { name: "Robert", planet: "Bomsky" },
  { name: "Robert", planet: "Bomsky" },
  { name: "Robert", planet: "Bomsky" },
];

export function Welcome() {
  const tableData: Person[] = mockData;

  const columns = useMemo<MRT_ColumnDef<Person>[]>(
    () => [
      {
        accessorKey: "name",
        header: "Name",
      },
      {
        accessorKey: "planet",
        header: "Planet",
      },
    ],
    []
  );

  return (
    <Box p={4}>
      <MaterialReactTable
        columns={columns}
        data={tableData}
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
