import { render, screen, waitFor } from "@testing-library/react";
import { Welcome } from "../welcome";
// @ts-ignore
import React, { act } from "react";
import "@testing-library/jest-dom";

jest.mock("../../infrastructure/api/dataApi", () => ({
  postSortingDataApi: jest.fn(() =>
    Promise.resolve({
      json: () =>
        Promise.resolve([
          { name: "Test Name", created: "2023-01-01T00:00:00.000Z" },
        ]),
    })
  ),
}));

jest.mock("material-react-table", () => ({
  MaterialReactTable: () => (
    <div data-testid="material-react-table">Mock Table</div>
  ),
}));

describe("Welcome Component", () => {
  it("renders without crashing", async () => {
    await act(async () => {
      render(<Welcome />);
    });

    // Tables should be in the document
    const tables = await screen.findAllByTestId("material-react-table");
    expect(tables).toHaveLength(2);

    // Algorithm select is present
    expect(screen.getByLabelText("Sorting Algorithm")).toBeInTheDocument();

    // Titles
    expect(screen.getByText("People")).toBeInTheDocument();
    expect(screen.getByText("Planets")).toBeInTheDocument();
  });

  it("fetches data from postSortingDataApi", async () => {
    const { postSortingDataApi } = await import("~/infrastructure/api/dataApi");

    render(<Welcome />);

    await waitFor(() => {
      expect(postSortingDataApi).toHaveBeenCalledWith("people", undefined);
      expect(postSortingDataApi).toHaveBeenCalledWith("planets", undefined);
    });
  });
});
