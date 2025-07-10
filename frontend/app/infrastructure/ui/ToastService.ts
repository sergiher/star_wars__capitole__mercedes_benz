export type ToastType = "info" | "error" | "success" | "warning";

export async function showToast(type: ToastType, message: string) {
  if (typeof window === "undefined") return;

  const { toast } = await import("react-toastify");
  toast[type](message);
}
