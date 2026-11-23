"use client";

import * as Primitive from "@radix-ui/react-dialog";
import { keepFocus, type OverlayDialogProps } from "./menu-dialog";
import { Dialog, DialogDescription, DialogPanel, DialogTitle } from "./ui/dialog";

export function ProfileDialog({ open, onClose }: OverlayDialogProps) {
  return (
    <Dialog open={open} onOpenChange={(next) => !next && onClose()}>
      <DialogPanel className="panel panel-notice" data-panel onCloseAutoFocus={keepFocus}>
        <div className="p-6">
          <DialogTitle className="type-entry">Profile</DialogTitle>
          <DialogDescription className="mt-3">
            Profile is not available in this mock. No sign-in or account data is used.
          </DialogDescription>
          <Primitive.Close className="button-primary mt-6" data-dialog-close>
            Close
          </Primitive.Close>
        </div>
      </DialogPanel>
    </Dialog>
  );
}
