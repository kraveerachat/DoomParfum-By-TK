// Generated pair: (en) and th render the same view with their locale (DPT-PLAN-013 4.2).
import { notFound } from "next/navigation";

/**
 * Target of the proxy rewrite for an address that cannot be decoded. A static segment, so no route
 * parameter is decoded from the malformed address; the response is the 404 unavailable view.
 */
export default function Unavailable() {
  notFound();
}
