import type { Metadata } from "next";
import Link from "next/link";
import { SyntheticNotice } from "@/components/mock-label";
import { fixtureSet } from "@/server/catalogue";

export const metadata: Metadata = { title: "About" };

const anchors = [
  { id: "purpose", label: "Purpose" },
  { id: "demonstrates", label: "What this mock demonstrates" },
  { id: "scope", label: "What remains future" },
  { id: "journal", label: "The scent notebook" },
  { id: "credits", label: "Local credits" },
] as const;

const section = "border-divider border-t pt-8 mt-12 w768:mt-16 w1024:mt-24";

export default function AboutPage() {
  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-10 w1024:pt-20">
        <div className="w1024:grid w1024:grid-cols-12 w1024:gap-x-6">
          <div className="w1024:col-span-8 w1024:col-start-3 w1280:col-start-3">
            <h1 className="type-page max-w-[16ch]">A notebook that says what it does not know.</h1>
            <p className="mt-6 max-w-[60ch]">
              DoomParfum By TK is planned as a private place to read about fragrance, follow notes and keep track of a
              collection. This is a mock of how that place could look and behave. Every record in it was invented.
            </p>
          </div>

          <nav
            aria-label="On this page"
            className="mt-8 w1024:col-span-8 w1024:col-start-3 w1280:col-span-2 w1280:col-start-1 w1280:row-span-2 w1280:row-start-1 w1280:mt-2"
          >
            <ul className="border-divider flex flex-col border-y py-2 w1280:border-b-0 w1280:border-t-ink">
              {anchors.map(({ id, label }) => (
                <li key={id}>
                  <Link
                    href={`#${id}`}
                    prefetch={false}
                    data-focus-key={`anchor-${id}`}
                    className="link-inline text-meta flex min-h-11 items-center py-1"
                  >
                    {label}
                  </Link>
                </li>
              ))}
            </ul>
          </nav>

          <div className="w1024:col-span-8 w1024:col-start-3 [&_p]:max-w-[60ch]">
            <section id="purpose" tabIndex={-1} data-route-target className={section} aria-labelledby="purpose-h">
              <h2 id="purpose-h" className="type-section">
                Purpose
              </h2>
              <p className="mt-5">
                A fragrance record mixes several kinds of information: what a thing is called, which notes it declares,
                what people say about it, who sells it and whether you own it. Those belong in different places. This
                notebook is designed so that none of them can stand in for another.
              </p>
            </section>

            <section id="demonstrates" tabIndex={-1} data-route-target className={section} aria-labelledby="demo-h">
              <h2 id="demo-h" className="type-section">
                What this mock demonstrates
              </h2>
              <ul className="mt-5 max-w-[60ch] [&>li]:border-divider [&>li]:border-b [&>li]:py-3">
                <li>Browsing and filtering a small set of fictional studies.</li>
                <li>Reading top, heart and base layers as labels, with general notes and accords kept apart.</li>
                <li>Following a note to every study that lists it.</li>
                <li>Telling an unknown field from one that was authored as empty.</li>
              </ul>
            </section>

            <section id="scope" tabIndex={-1} data-route-target className={section} aria-labelledby="scope-h">
              <h2 id="scope-h" className="type-section">
                What remains future
              </h2>
              <p className="mt-5">
                Nothing here connects to a real catalogue, an account or a store. Scent matching, the private catalogue,
                permission to use outside sources, account security, the cart and the collection are separate pieces of
                work. Each has its own approval, and this mock approves none of them.
              </p>
              <p className="mt-4">
                The mock runs on one computer. It asks search engines not to index it, and that request is not a
                security control.
              </p>
            </section>

            <section id="journal" tabIndex={-1} data-route-target className={section} aria-labelledby="journal-h">
              <h2 id="journal-h" className="type-section">
                The scent notebook
              </h2>
              <p className="text-text-secondary mt-5">
                Two sample articles about reading this mock. They make no claim about any real product.
              </p>
              {fixtureSet.articles.map((article) => (
                <article
                  key={article.id}
                  id={article.anchor}
                  tabIndex={-1}
                  data-route-target
                  aria-labelledby={`${article.id}-h`}
                  className="mt-12 scroll-mt-8"
                >
                  <h3 id={`${article.id}-h`} className="type-entry">
                    {article.title}
                  </h3>
                  <p className="mt-3 font-medium">{article.excerpt}</p>
                  {article.body.map((paragraph) => (
                    <p key={paragraph.slice(0, 24)} className="mt-5">
                      {paragraph}
                    </p>
                  ))}
                </article>
              ))}
            </section>

            <section id="credits" tabIndex={-1} data-route-target className={section} aria-labelledby="credits-h">
              <h2 id="credits-h" className="type-section">
                Local credits
              </h2>
              <p className="mt-5">
                The drawings, records and articles were made for this project. Type is set in Bodoni Moda and Noto Sans
                Thai under the SIL Open Font License 1.1, and icons come from Lucide under the ISC license. All of it is
                served from this computer.
              </p>
            </section>
          </div>
        </div>
      </div>
    </>
  );
}
