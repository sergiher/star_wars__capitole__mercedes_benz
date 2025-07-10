export async function fetchAiInsightApi(
  entityType: string,
  name: string
): Promise<string> {
  const baseUrl = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";
  const response = await fetch(
    `${baseUrl}/simulate-ai-insight/${entityType}/${encodeURIComponent(name)}`,
    { method: "POST" }
  );

  if (!response.ok) {
    const err = await response.text();
    throw new Error(err);
  }
  return await response.text();
}
