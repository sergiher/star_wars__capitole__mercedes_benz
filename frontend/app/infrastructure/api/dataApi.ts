export async function getPeopleDataApi() {
  const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/people`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error(`Failed to get people data`);
  }

  return response;
}

export async function postSortingDataApi(
  sortParams: {
    field: string;
    direction: string;
  }[]
) {
  const response = await fetch(
    `${import.meta.env.VITE_API_BASE_URL}/sort/people`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        field: sortParams[0]?.field ?? "name",
        direction: sortParams[0]?.direction ?? "asc",
        algorithm: "power_sort",
      }),
    }
  );

  if (!response.ok) {
    throw new Error(`Failed to sort data`);
  }

  return response;
}
