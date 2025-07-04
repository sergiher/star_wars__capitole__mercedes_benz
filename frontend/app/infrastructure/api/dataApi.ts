export async function getPeopleDataApi() {
  const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/people`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error(`Failed to get people data`);
  }

  return response;
}
