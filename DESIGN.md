---
name: Alberto Robazza Portfolio
description: A personal portfolio for an AI Researcher & Engineer with a documented, technical identity.
colors:
  bg-deep: "#0b0f19"
  bg-alt: "#131a2a"
  text-main: "#f8fafc"
  text-muted: "#94a3b8"
  accent: "#38bdf8"
  border: "#1e293b"
typography:
  display:
    fontFamily: "Outfit, sans-serif"
    fontSize: "clamp(4rem, 8vw, 6rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Outfit, sans-serif"
    fontSize: "clamp(2rem, 3vw + 1rem, 2.5rem)"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Outfit, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  mono:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "0.9rem"
    fontWeight: 400
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "0.75rem"
    fontWeight: 700
    textTransform: "uppercase"
    letterSpacing: "0.05em"
rounded:
  sm: "3px"
  md: "4px"
  lg: "8px"
spacing:
  sm: "0.5rem"
  md: "1rem"
  lg: "2rem"
  xl: "3rem"
  xxl: "4rem"
components:
  link-primary:
    color: "{colors.accent}"
    textDecoration: "none"
    transition: "color 0.3s ease"
  link-primary-hover:
    color: "#7dd3fc"
  card-default:
    backgroundColor: "{colors.bg-alt}"
    border: "1px solid {colors.border}"
    borderRadius: "{rounded.lg}"
    padding: "1.5rem"
  nav-fixed:
    backgroundColor: "rgba(11, 15, 25, 0.85)"
    backdropFilter: "blur(10px)"
    borderBottom: "1px solid {colors.border}"
    zIndex: 1000
---

# Design System: Alberto Robazza Portfolio

## 1. Overview

**Creative North Star: "The Hacker's Notebook"**

This design system is documented, methodical, and technical. It treats the portfolio like a written log, a research notebook, or a pen-tester's report. Every element is deliberate, every interaction has a reason, and the visual language speaks the dialect of someone who works in AI and cybersecurity. The system rejects SaaS landing-page clichés. It rejects the noise of generic developer portfolios. It commits to a dark, precise, terminal-flavored aesthetic that signals deep technical work without theatrics.

The system is **Layered, Lab-Confident**. Surfaces carry subtle depth (box-shadows, tonal borders) to suggest dimension even at rest. The accent color (Electric Ice) is used with surgical precision, never as decoration. Typography pairs a geometric sans (Outfit) for body and display with a technical mono (JetBrains Mono) for labels, dates, and code. The result is a portfolio that reads as a working tool, not a marketing page.

**Key Characteristics:**
- Dark navy background (#0b0f19) with near-black alternates (#131a2a)
- Sky-blue accent (#38bdf8) used for links, active states, and emphasis
- Monospace labels for metadata (dates, tags, keyboard shortcuts)
- Connected vertical highlights list (not card grids)
- Left-aligned hero with code snippet overlay
- Keyboard-first navigation with `g` + key shortcuts
- Layered depth via subtle shadows and tonal borders

## 2. Colors

The palette is dark, technical, and committed. The base is a deep navy that borders on black; the accent is a cold, electric blue that reads as precision instrument.

### Primary
- **Electric Ice** (#38bdf8): The single accent color. Used for links, active nav states, timeline dots, badge borders, and emphasis. Cold, sharp, and precise. Never used as a background fill (except for the keyboard help overlay scrim).

### Neutral
- **Deep Navy** (#0b0f19): Primary body background. The surface of the notebook.
- **Tonal Navy** (#131a2a): Alternate background for section breaks. Used for `.bg-alt` sections and card backgrounds. Creates tonal layering.
- **Off-White** (#f8fafc): Primary text. High contrast (18.3:1) against Deep Navy.
- **Muted Gray** (#94a3b8): Secondary text. Used for taglines, metadata, and supporting copy. Contrast 7.47:1 (well above WCAG AA).
- **Border Gray** (#1e293b): Dividers, card borders, and subtle separators. Tonal, not decorative.

### Named Rules

**The One Accent Rule.** Electric Ice is the only color that commands attention. It is used on links, active states, and emphasis, never as background fill (except the help overlay scrim). Its rarity is the point.

**The Muted Gray Rule.** Body text is never pure gray. It is always Muted Gray (#94a3b8), which carries 7.47:1 contrast against Deep Navy. The muted tone signals secondary information without sacrificing readability.

## 3. Typography

**Display Font:** Outfit (with sans-serif fallback). A geometric sans with technical clarity, used for h1 and h2.

**Body Font:** Outfit (with sans-serif fallback). The same family for body keeps the system tight. Weights 400 (body) and 600/800 (headings).

**Label/Mono Font:** JetBrains Mono (with monospace fallback). Used for dates, tags, keyboard shortcuts, code snippets, and any metadata. Its technical character reinforces the system identity.

**Character:** Clean, geometric, precise. The pairing is not decorative; it is functional. Outfit carries the voice, JetBrains Mono carries the metadata.

### Hierarchy
- **Display** (800, clamp(4rem, 8vw, 6rem), 1.0): Hero h1. The name. Capped at 6rem to avoid shouting.
- **Headline** (600, clamp(2rem, 3vw + 1rem, 2.5rem), 1.1): Section titles. Includes left accent bar.
- **Title** (600, 1.5rem, 1.1): Card titles, h3 in content. Monospace for highlight content h3.
- **Body** (400, 1rem, 1.6): Paragraphs. Max-width 70ch for line length.
- **Label** (700, 0.75rem, 0.05em, uppercase): Dates, tags, kicker text. Monospace family.

### Named Rules

**The Pairing Rule.** One sans family for body and display. One mono family for metadata. Never pair two similar sans-serifs. The contrast between geometric sans and technical mono carries the system identity.

**The Display Ceiling Rule.** Hero h1 never exceeds 6rem (96px). It commands the eye at any viewport, but it does not shout. The clamp() range (4rem to 6rem) keeps it readable on mobile without losing presence on desktop.

## 4. Elevation

This system is **Always Layered**. Surfaces carry subtle depth at rest, not just on hover. Depth is conveyed through:

- Tonal background shifts (Deep Navy → Tonal Navy) for section breaks
- Subtle box-shadows on cards and blog posts at rest
- 1px tonal borders (Border Gray) for subtle separation
- Glow effects on accent elements (timeline dots, hover states)

### Shadow Vocabulary
- **Card Shadow** (`box-shadow: 0 5px 20px rgba(0,0,0,0.3)`): Blog post cards. Subtle, ambient. Appears on hover.
- **Glow** (`box-shadow: 0 0 10px var(--accent-glow)`): Timeline dots, focus rings. Accent-tinted. Suggests activity.
- **Scrim** (`background: rgba(11, 15, 25, 0.9)`): Keyboard help overlay backdrop. Blurs the page behind it.

### Named Rules

**The Layered Rule.** Surfaces are layered at rest. Shadow + tonal shift + border combine to create depth without relying on a single dramatic effect.

**The Glow Rule.** Glows are accent-tinted, not white. They suggest activity, not decoration. Used only on interactive elements (timeline dots, focus rings, hover states).

## 5. Components

### Buttons & Links
- **Shape:** No explicit border-radius on links. Buttons (if added) use 4px radius.
- **Primary:** Color Electric Ice (#38bdf8). No background fill. Underline on hover only if text is long-form.
- **Hover:** Color shifts to #7dd3fc (lighter accent). 0.3s transition.
- **Mono Link (Blog nav):** JetBrains Mono, prefixed with `>`. Borderless. The terminal command style.

### Cards & Containers
- **Corner Style:** 8px radius (lg).
- **Background:** Tonal Navy (#131a2a) for timeline content; Deep Navy for blog posts.
- **Border:** 1px Border Gray (#1e293b) for separation.
- **Shadow:** Card shadow on hover only for blog posts; timeline content uses border + background only.
- **Internal Padding:** 1.5rem for timeline content; 2rem for blog posts.

### Navigation
- **Style:** Fixed top bar. Dark scrim (rgba(11, 15, 25, 0.85)) with 10px backdrop blur. Border-bottom 1px Border Gray.
- **Typography:** Outfit, 0.95rem, weight 500, uppercase, 1px letter-spacing. Muted Gray default; Electric Ice on hover and active.
- **Active State:** IntersectionObserver highlights the current section's link. Electric Ice color.
- **Highlight Link (Blog):** Monospace terminal style with `>` prefix. Distinguishes the primary CTA.
- **Mobile:** Slide-in panel from right (70% width, max 300px). Hamburger toggle with X animation. Closes on link click or backdrop tap.

### Timeline
- **Style:** Vertical line (2px Border Gray) with dots (14px circles) at each entry. Dot has Electric Ice background and accent glow.
- **Date:** JetBrains Mono, 0.9rem, Electric Ice. Sits above the entry card.
- **Content Card:** Tonal Navy background, 1px border, 8px radius, 1.5rem padding.

### Skills Tags
- **Style:** Pill-shaped. Background: rgba(56, 189, 248, 0.1) (accent tint). Border: 1px rgba(56, 189, 248, 0.2). Text: Electric Ice, JetBrains Mono, 0.85rem. Padding: 0.4rem 0.8rem.

### Keyboard Help Overlay
- **Trigger:** `?` key.
- **Style:** Fixed full-screen. Background: rgba(11, 15, 25, 0.9) with backdrop blur. Content card: 400px max-width, Tonal Navy background, 1px border, 8px radius.
- **Typography:** JetBrains Mono for shortcut keys (kbd elements), Outfit for descriptions.
- **Close:** `Esc` key, click outside the content card, or `?` again.

## 6. Do's and Don'ts

### Do:
- **Do** use the existing CSS tokens (`--bg-color`, `--accent`, etc.) for all color and spacing values. No hard-coded hex in component CSS.
- **Do** pair the geometric sans (Outfit) for body with the technical mono (JetBrains Mono) for metadata. This pairing carries the system identity.
- **Do** use `text-wrap: balance` on h1–h3 and `text-wrap: pretty` on long prose to reduce orphans.
- **Do** cap hero h1 at 6rem via `clamp(4rem, 8vw, 6rem)`. It commands the eye without shouting.
- **Do** respect `prefers-reduced-motion` for all transitions and animations. The scroll-hint, nav toggle, and blog hover effects all have reduced-motion fallbacks.
- **Do** add `aria-hidden="true"` to decorative icons (SVG, Font Awesome). The text next to them provides the meaning.
- **Do** use the keyboard shortcut system (`g` + key) for power-user navigation. Press `?` to show the help overlay.

### Don't:
- **Don't** use the identical 3-column card grid cliché. The highlights section uses a connected vertical list with a line between icons.
- **Don't** add the "System Ready" badge, "About" / "Process" / "Pricing" eyebrows, or any SaaS template scaffolding. The system rejects these by design.
- **Don't** use border-left or border-right as colored stripes on cards, list items, or callouts. Rewrite with full borders, background tints, or nothing.
- **Don't** use gradient text (`background-clip: text`). Use a single solid color. Emphasis via weight or size.
- **Don't** use glassmorphism as a default. Blurs are functional (navbar scrim, help overlay backdrop), not decorative.
- **Don't** pair two similar sans-serifs. The system uses one sans family and one mono family. That's it.
- **Don't** use border-left stripes on the section titles. The accent bar is positioned via `::before` on the left, not as a border property.
- **Don't** use the em-dash as a dramatic reveal. Use commas, periods, or parentheses. The blog content has been audited for AI patterns.
- **Don't** use the "navigate" verb in visible prose. It appears in JavaScript function names (`navigateTo`) but is banned from user-facing copy.
- **Don't** use Inter, Roboto, or any reflex-pick font. The system uses Outfit and JetBrains Mono, both distinctive choices.
