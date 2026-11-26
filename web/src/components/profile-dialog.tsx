"use client";

import * as Primitive from "@radix-ui/react-dialog";
import { useT } from "@/i18n/client";
import { keepFocus, type OverlayDialogProps } from "./menu-dialog";
import { Dialog, DialogDescription, DialogPanel, DialogTitle } from "./ui/dialog";

export function ProfileDialog({ open, onClose }: OverlayDialogProps) {
  const t = useT();
  return (
    <Dialog open={open} onOpenChange={(next) => !next && onClose()}>
      <DialogPanel className="panel panel-notice" data-panel onCloseAutoFocus={keepFocus}>
        <div className="p-6">
          <DialogTitle className="type-entry">{t.profile.title}</DialogTitle>
          <DialogDescription className="mt-3">{t.profile.text}</DialogDescription>
          <Primitive.Close className="button-primary mt-6" data-dialog-close>
            {t.nav.close}
          </Primitive.Close>
        </div>
      </DialogPanel>
    </Dialog>
  );
}
