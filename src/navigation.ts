/**
 * Navigation functionality for document sections
 * Provides back navigation when users navigate via anchor links
 */

interface NavigationState {
	history: string[];
	currentIndex: number;
}

const navigationState: NavigationState = {
	history: [],
	currentIndex: -1
};

function recordNavigation(newHash: string): void {
	if(navigationState.history.length === 0 ||
		navigationState.history[navigationState.history.length - 1] !== newHash) {

		// Remove any forward history if we're not at the end
		if(navigationState.currentIndex < navigationState.history.length - 1) {
			navigationState.history = navigationState.history.slice(0, navigationState.currentIndex + 1);
		}

		navigationState.history.push(newHash);
		navigationState.currentIndex = navigationState.history.length - 1;
	}
}

function handleHashChange(event: HashChangeEvent): void {
	const newHash = window.location.hash;
	const oldHash = new URL(event.oldURL).hash;

	if(oldHash !== newHash) {
		recordNavigation(oldHash);
	}
}

function handlePopState(): void {
	// Browser back/forward navigation handled automatically
}

function setupInternalLinks(): void {
	const internalLinks = document.querySelectorAll('a[href^="#"]');

	internalLinks.forEach((link) => {
		link.addEventListener('click', () => {
			const currentHash = window.location.hash;
			if(currentHash) {
				recordNavigation(currentHash);
			}
		});
	});
}

function initializeNavigation(): void {
	window.addEventListener('hashchange', handleHashChange);
	window.addEventListener('popstate', handlePopState);

	setupInternalLinks();

	// Record initial state if we start with a hash
	if(window.location.hash) {
		recordNavigation(''); // Empty string represents top of page
	}
}

// Initialize when DOM is ready
if(document.readyState === 'loading') {
	document.addEventListener('DOMContentLoaded', initializeNavigation);
} else {
	initializeNavigation();
}

export { initializeNavigation };