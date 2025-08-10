# GitHub Copilot Instructions

## Code Quality Guidelines

### Comment Philosophy
- **Avoid obvious comments** for self-explanatory code
- Function names should clearly indicate their purpose
- Only comment complex business logic or non-obvious behavior
- Prefer descriptive function/variable names over explanatory comments

### Examples of What NOT to Comment:

❌ **Bad - Obvious comments:**
```typescript
// Handle back/forward browser buttons
window.addEventListener('popstate', this.handlePopState.bind(this));

// Add click handlers to all anchor links
this.setupInternalLinks();

// Navigate to document top
window.location.hash = '';
```

✅ **Good - Self-explanatory code:**
```typescript
window.addEventListener('popstate', this.handlePopState.bind(this));
this.setupInternalLinks();
window.location.hash = '';
```

### When TO Comment:

✅ **Complex business logic:**
```typescript
// Extract hash from oldURL since HashChangeEvent.oldURL includes full URL
const oldHash = event.oldURL.split('#')[1] || null;
```

✅ **Non-obvious behavior:**
```typescript
// Preserve navigation history for multi-level back navigation
if (oldHash && oldHash !== newHash.substring(1)) {
  this.state.previousHash = oldHash;
  this.state.navigationHistory.push(oldHash);
}
```

## TypeScript Guidelines

### Function Naming
- Use descriptive verbs that clearly indicate the action
- `handleHashChange()` instead of `onHashChange()`
- `updateBackButtons()` instead of `setButtons()`
- `canNavigateBack()` instead of `checkBack()`

### Interface Design
- Use clear, descriptive property names
- Document complex interfaces with JSDoc
- Prefer explicit types over `any`

### Code Organization
- Group related functionality in files
- Prefer functional style over OOP, unless there is state to store in the class
- Export only what's needed by other modules
- **Remove unused files** - delete files when their references are removed

## File Management
- When removing functionality, also remove associated files (CSS, assets, etc.)
- Keep the project clean by eliminating dead code and unused assets
- Update imports/references when moving or deleting files
- Regularly audit for orphaned files that serve no purpose

## Project Structure
- Source code in `src/` directory
- Separate concerns: navigation, styling, content
- Follow TypeScript project conventions
