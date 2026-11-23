"use client";

/**
 * shadcn/ui-style wrapper over the Radix dialog primitive. The Radix overlay part is not used:
 * it injects a style element that the nonce CSP would reject. Scroll lock and scrim are plain CSS.
 */
import * as Primitive from "@radix-ui/react-dialog";
import { X } from "lucide-react";
import type { ComponentProps, ReactNode } from "react";

export const Dialog = Primitive.Root;
export const DialogTitle = Primitive.Title;
export const DialogDescription = Primitive.Description;

export function DialogPanel({ children, ...props }: ComponentProps<typeof Primitive.Content>) {
  return (
    <Primitive.Portal>
      <Primitive.Content {...props}>{children}</Primitive.Content>
    </Primitive.Portal>
  );
}

export function DialogHeader({ children }: { children: ReactNode }) {
  return (
    <div className="flex items-center justify-between gap-4 ps-4 pe-2 pt-3 pb-2">
      {children}
      <Primitive.Close className="icon-button" aria-label="Close" data-dialog-close>
        <X aria-hidden="true" size={20} strokeWidth={1.5} />
      </Primitive.Close>
    </div>
  );
}
