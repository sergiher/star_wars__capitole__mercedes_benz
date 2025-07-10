import { useEffect, useState } from "react";

let ToastContainer: any = null;

export function ClientToastContainer() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    import("react-toastify").then((mod) => {
      ToastContainer = mod.ToastContainer;
      import("react-toastify/dist/ReactToastify.css");
      setMounted(true);
    });
  }, []);

  if (!mounted || !ToastContainer) return null;

  return <ToastContainer />;
}
