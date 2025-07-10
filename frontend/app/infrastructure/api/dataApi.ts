export async function postSortingDataApi(
  entity_type: string,
  sortParams?: {
    field: string;
    direction: string;
    algorithm: string;
  }[]
) {
  const hasSorting = sortParams && sortParams.length > 0;
  const baseUrl = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";
  const response = await fetch(`${baseUrl}/sort/${entity_type}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    ...(hasSorting && {
      body: JSON.stringify({
        field: sortParams[0]?.field ?? "name",
        direction: sortParams[0]?.direction ?? "asc",
        ...(sortParams[0]?.algorithm && {
          algorithm: sortParams[0].algorithm,
        }),
      }),
    }),
  });

  if (!response.ok) {
    throw new Error(`Failed to sort data`);
  }

  return response;
}
