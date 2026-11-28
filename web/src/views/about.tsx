import type { Metadata } from "next";
import { AboutContents } from "@/components/about-contents";
import { SyntheticNotice } from "@/components/mock-label";
import type { Locale } from "@/i18n/locale";
import { MESSAGES } from "@/i18n/messages";
import { articlesFor } from "@/server/catalogue";

export const aboutMetadata = (locale: Locale): Metadata => ({ title: MESSAGES[locale].titles.about });

const rule = "rule-section pt-8 mt-12";
// The short explanations sit closer together than the notebook and the credits.
const brief = `${rule} w1024:mt-16`;
const major = `${rule} w768:mt-16 w1024:mt-24`;

export function AboutView({ locale }: { locale: Locale }) {
  const t = MESSAGES[locale].about;
  const articles = articlesFor(locale);
  const anchors = [
    { id: "purpose", label: t.purpose },
    { id: "demonstrates", label: t.demonstrates },
    { id: "scope", label: t.scope },
    { id: "journal", label: t.journal },
    { id: "credits", label: t.credits },
  ];

  return (
    <>
      <SyntheticNotice />
      <div className="wrap pt-10 w1024:pt-20">
        <div className="w1024:grid w1024:grid-cols-12 w1024:gap-x-6">
          <div className="w1024:col-span-8 w1024:col-start-3">
            <h1 className="type-page max-w-[16ch]">{t.h1}</h1>
            <p className="type-long mt-6 max-w-[60ch]">{t.lead}</p>
          </div>

          <div className="mt-8 w1024:col-span-8 w1024:col-start-3 w1280:col-span-2 w1280:col-start-1 w1280:row-span-2 w1280:row-start-1 w1280:mt-2 w1280:self-stretch">
            <AboutContents anchors={anchors} />
          </div>

          <div className="type-long w1024:col-span-8 w1024:col-start-3 [&_p]:max-w-[62ch] [&_p:lang(th)]:max-w-[36em]">
            <section id="purpose" tabIndex={-1} data-route-target className="mt-2 pt-8 w1280:mt-16 w1280:rule-section" aria-labelledby="purpose-h">
              <h2 id="purpose-h" className="type-section">
                {t.purpose}
              </h2>
              <p className="mt-5">{t.purposeText}</p>
            </section>

            <section id="demonstrates" tabIndex={-1} data-route-target className={brief} aria-labelledby="demo-h">
              <h2 id="demo-h" className="type-section">
                {t.demonstrates}
              </h2>
              <ul className="mt-5 max-w-[62ch] [&>li]:border-divider [&>li]:border-b [&>li]:py-3 [&>li:last-child]:border-b-0 [&>li:last-child]:pb-0">
                <li>{t.demo1}</li>
                <li>{t.demo2}</li>
                <li>{t.demo3}</li>
                <li>{t.demo4}</li>
              </ul>
            </section>

            <section id="scope" tabIndex={-1} data-route-target className={brief} aria-labelledby="scope-h">
              <h2 id="scope-h" className="type-section">
                {t.scope}
              </h2>
              <p className="mt-5">{t.scopeText1}</p>
              <p className="mt-4">{t.scopeText2}</p>
            </section>

            <section id="journal" tabIndex={-1} data-route-target className={major} aria-labelledby="journal-h">
              <h2 id="journal-h" className="type-section">
                {t.journal}
              </h2>
              <p className="text-text-secondary mt-5">{t.journalText}</p>
              {articles.map((article) => (
                <article
                  key={article.id}
                  id={article.anchor}
                  tabIndex={-1}
                  data-route-target
                  aria-labelledby={`${article.id}-h`}
                  className="border-divider mt-10 max-w-[62ch] border-t pt-8"
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

            <section id="credits" tabIndex={-1} data-route-target className={major} aria-labelledby="credits-h">
              <h2 id="credits-h" className="type-section">
                {t.credits}
              </h2>
              <p className="mt-5">{t.creditsText}</p>
            </section>
          </div>
        </div>
      </div>
    </>
  );
}
