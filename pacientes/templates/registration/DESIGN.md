---
name: Warm Modern Veterinary
colors:
  surface: '#f3fcf4'
  surface-dim: '#d3dcd5'
  surface-bright: '#f3fcf4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#edf6ee'
  surface-container: '#e7f0e9'
  surface-container-high: '#e1eae3'
  surface-container-highest: '#dce5dd'
  on-surface: '#151d19'
  on-surface-variant: '#3f4945'
  inverse-surface: '#2a322d'
  inverse-on-surface: '#eaf3ec'
  outline: '#6f7974'
  outline-variant: '#bfc9c3'
  surface-tint: '#246a56'
  primary: '#1d6450'
  on-primary: '#ffffff'
  primary-container: '#3a7d68'
  on-primary-container: '#dcfff0'
  inverse-primary: '#90d4bb'
  secondary: '#9a442d'
  on-secondary: '#ffffff'
  secondary-container: '#fc9174'
  on-secondary-container: '#742814'
  tertiary: '#775100'
  on-tertiary: '#ffffff'
  tertiary-container: '#976800'
  on-tertiary-container: '#fff5eb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#acf1d7'
  primary-fixed-dim: '#90d4bb'
  on-primary-fixed: '#002118'
  on-primary-fixed-variant: '#00513f'
  secondary-fixed: '#ffdbd2'
  secondary-fixed-dim: '#ffb4a1'
  on-secondary-fixed: '#3c0800'
  on-secondary-fixed-variant: '#7c2e19'
  tertiary-fixed: '#ffdead'
  tertiary-fixed-dim: '#fabc4d'
  on-tertiary-fixed: '#281900'
  on-tertiary-fixed-variant: '#604100'
  background: '#f3fcf4'
  on-background: '#151d19'
  surface-variant: '#dce5dd'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 34px
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-mobile: 0.75rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system expresses compassionate clinical excellence: reassuring, warm, deeply competent, and tactile. It balances medical credibility with the comforting gentleness required when pet guardians seek veterinary care. 

The aesthetic fuses contemporary clean minimalism with organic, soft-touch tactile design. Visual density is intentionally light and unhurried. Layouts prioritize rapid legibility on mobile devices, low-anxiety visual hierarchy, and inviting micro-interactions that evoke trust, hygiene, and genuine affection for animals.

## Colors

The color palette centers on therapeutic natural tones balanced by energetic, caring accents:

- **Primary (`#3A7D68` - Sage Emerald):** Communicates clinical integrity, natural healing, and botanical tranquility. Used for primary actions, critical brand touchpoints, active states, and focal iconography.
- **Secondary (`#E07A5F` - Soft Coral):** Delivers warmth, heartbeat vitality, and compassionate urgency. Used for primary appointment prompts, vaccination alerts, high-importance highlights, and badges.
- **Tertiary (`#E5A93C` - Honey Amber):** Expresses cheerful warmth, pet wellness tracking, reward badges, and preventive reminders.
- **Neutral (`#707973` - Sage Mineral):** A soft, desaturated slate-sage used for balanced body copy, subtle divider lines, and neutral surface grounding.
- **Canvas & Backgrounds:** Crisp warm ivory (`#FAF9F5`) and muted clinical mist (`#F0F4F1`) serve as primary canvas and container layers, banishing cold, sterile hospital whites in favor of domestic comfort.

## Typography

**Plus Jakarta Sans** is selected across display, body, and label roles. Its geometric underpinnings combined with warm, humanist terminals create an accessible, contemporary atmosphere without sacrificing legibility on small touchscreens.

- **Weight Distinctions:** Headlines use 600 and 700 weights to establish confident anchor points during stressful clinical scenarios (e.g., emergency bookings, triage triage forms).
- **Body & Captions:** Kept at weight 400 with open aperture spacing to maintain quick reading speeds under direct sunlight or movement.
- **Labels & Microcopy:** Weight 600 provides quick visual scanning for pet vitals, date pickers, vaccine dates, and form labels.

## Layout & Spacing

The layout model utilizes a fluid 12-column grid for desktop views (max-width 1200px) and transitions to a responsive 4-column fluid grid on mobile devices. 

- **Touch Ergonomics:** Interactive targets respect a minimum bounding zone of 48×48px with generous spacing (`space-sm` to `space-md`) between interactive pills, chips, and quick-action slots to prevent mis-taps.
- **Rhythm:** Section stacking employs `space-xl` on mobile and `space-xl` doubled on desktop to give medical forms, animal health timelines, and profiles clarity without clutter.
- **Safe Insets:** Mobile layouts feature bottom sheet padding and navigation docks with integrated safe-area inset preservation.

## Elevation & Depth

Visual hierarchy uses ultra-soft ambient layering rather than aggressive dark shadows or clinical flat outlines:

- **Level 0 (Base Canvas):** Warm tinted surface (`#FAF9F5`).
- **Level 1 (Surface Cards & Containers):** Solid pure white (`#FFFFFF`) or tinted porcelain mist (`#F4F7F5`) resting on base canvas, accompanied by a tinted ambient shadow: `0 4px 20px -2px rgba(58, 125, 104, 0.06)`.
- **Level 2 (Floating Modals, Bottom Sheets & Popovers):** Elevated with an expanded diffuse drop shadow: `0 12px 36px -4px rgba(45, 74, 65, 0.12)`.
- **Borders:** Low-contrast ghost borders (`1px solid rgba(58, 125, 104, 0.08)`) encase cards and input states, preserving tactile structure without visual noise.

## Shapes

The shape system adopts friendly, organic geometry configured at level 2 (`rounded-2xl` for containers and cards).

- **Standard Cards and Sheets:** Set with `1rem` to `1.5rem` (`rounded-xl` to `rounded-2xl`) corner radiuses to reinforce friendliness and remove sharp clinical edges.
- **Buttons and Chips:** Employ full-pill contours (`9999px`) or soft `rounded-xl` perimeters for an intuitive, inviting touch sensation.
- **Pet Avatar Frames & Badges:** Rounded squircle shapes (corner-smoothing enabled where supported) to highlight patient photos with softness.

## Components

### Buttons
- **Primary:** Filled in `#3A7D68` with crisp white text, full-pill or `rounded-xl` radius, generous horizontal padding (`space-lg`), and subtle depressed micro-transition upon tap.
- **Secondary (Caring / Urgent Actions):** Filled in `#E07A5F` with white typography for primary scheduling actions, renewals, and hotlines.
- **Tertiary / Ghost:** Transparent background with `#3A7D68` text and a subtle warm border (`rgba(58, 125, 104, 0.15)`).

### Input Fields & Selectors
- Background filled with warm neutral-white (`#FBFBF9`), bounded by an ultra-thin sage-tinted border (`#E2E8E4`).
- Focus state brings a 2px inner ring in `#3A7D68` with a soft outer glow (`rgba(58, 125, 104, 0.12)`). Labels rest prominently above in `label-md` weight 600.

### Cards & Pet Records
- White background (`#FFFFFF`), `rounded-2xl` contouring, and level 1 ambient emerald shadow.
- Header incorporates a squircle avatar for patient species/photo, an inline status chip (e.g., "Vaccines Up-to-Date" in primary sage or "Checkup Due" in amber), and an organic divider line.

### Chips & Filter Pills
- Compact, pill-shaped tags used for species filtering (Dogs, Cats, Exotics), available slots, and doctor specializations. 
- Inactive state: `#F0F4F1` background with `#3A7D68` label. 
- Active state: `#3A7D68` background with crisp white label and subtle scale punch.

### Checkboxes & Radios
- Distinctively rounded check squares and circles with a 2px sage boundary. Checked state fills with `#3A7D68` displaying a white, bold checkmark icon.

### Specialized Veterinary Components
- **Pet Health Timeline:** Vertical stacked cards connected by an organic dotted sage trace line, featuring colored milestone nodes (Coral for clinical surgeries, Amber for nutrition/deworming, Emerald for routine wellness checks).
- **Appointment Quick-Slot Bar:** Horizontally scrolling mobile bar featuring rounded squircle calendar days with live availability badges.