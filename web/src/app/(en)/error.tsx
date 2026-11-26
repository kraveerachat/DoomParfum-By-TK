"use client";

import { RenderErrorView } from "@/views/system";

export default function RenderError({ retry }: { error: Error; retry: () => void }) {
  return <RenderErrorView retry={retry} />;
}
