import { toast } from "react-toastify";

export const notifyMessage = (infoMessage: string) => {
  toast.info(infoMessage, { autoClose: false });
};

export const notifyError = (errorMessage: string) => {
  toast.error(errorMessage, { autoClose: 15000 });
};
