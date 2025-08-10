// back-navigation.ts

interface BackNavigation {
  init(): void;
  destroy(): void;
}

class AnchorBackNavigation implements BackNavigation {
  private backButton: HTMLElement | null = null;
  private navigationHistory: string[] = [];
  private currentIndex: number = -1;

  init(): void {
    this.createBackButton();
    this.setupEventListeners();
    this.handleInitialHash();
  }

  private createBackButton(): void {
    // Create back button
    const backBtn = document.createElement('button');
    backBtn.id = 'back-nav-btn';
    backBtn.innerHTML = '← Back';
    backBtn.style.cssText = `
      position: fixed;
      top: 20px;
      right: 20px;
      z-index: 1000;
      padding: 8px 16px;
      background: #007cba;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      display: none;
      box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    `;
    
    backBtn.addEventListener('click', () => this.goBack());
    document.body.appendChild(backBtn);
    this.backButton = backBtn;
  }

  private setupEventListeners(): void {
    // Listen for hash changes (anchor navigation)
    window.addEventListener('hashchange', (event) => {
      this.handleHashChange(event.oldURL, event.newURL);
    });

    // Listen for anchor clicks
    document.addEventListener('click', (event) => {
      const target = event.target as HTMLElement;
      const anchor = target.closest('a[href^="#"]') as HTMLAnchorElement;
      
      if (anchor && anchor.hash) {
        this.recordNavigation(window.location.hash, anchor.hash);
      }
    });
  }

  private handleInitialHash(): void {
    if (window.location.hash) {
      this.navigationHistory = ['', window.location.hash];
      this.currentIndex = 1;
      this.updateBackButtonVisibility();
    }
  }

  private handleHashChange(oldURL: string, newURL: string): void {
    const oldHash = this.extractHash(oldURL);
    const newHash = this.extractHash(newURL);
    
    if (oldHash !== newHash) {
      this.recordNavigation(oldHash, newHash);
    }
  }

  private extractHash(url: string): string {
    const hashIndex = url.indexOf('#');
    return hashIndex !== -1 ? url.substring(hashIndex) : '';
  }

  private recordNavigation(fromHash: string, toHash: string): void {
    // Remove any forward history if we're not at the end
    if (this.currentIndex < this.navigationHistory.length - 1) {
      this.navigationHistory = this.navigationHistory.slice(0, this.currentIndex + 1);
    }
    
    // Add new navigation
    if (this.navigationHistory.length === 0 || this.navigationHistory[this.navigationHistory.length - 1] !== fromHash) {
      this.navigationHistory.push(fromHash);
    }
    
    this.navigationHistory.push(toHash);
    this.currentIndex = this.navigationHistory.length - 1;
    
    this.updateBackButtonVisibility();
  }

  private goBack(): void {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      const previousHash = this.navigationHistory[this.currentIndex];
      
      // Navigate without triggering hashchange event
      history.replaceState(null, '', previousHash || window.location.pathname);
      
      // Scroll to element if hash exists
      if (previousHash) {
        const targetElement = document.querySelector(previousHash);
        if (targetElement) {
          targetElement.scrollIntoView({ behavior: 'smooth' });
        }
      } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
      
      this.updateBackButtonVisibility();
    }
  }

  private updateBackButtonVisibility(): void {
    if (this.backButton) {
      this.backButton.style.display = this.currentIndex > 0 ? 'block' : 'none';
    }
  }

  destroy(): void {
    if (this.backButton) {
      this.backButton.remove();
      this.backButton = null;
    }
    this.navigationHistory = [];
    this.currentIndex = -1;
  }
}

// Initialize the back navigation
const backNav = new AnchorBackNavigation();
document.addEventListener('DOMContentLoaded', () => {
  backNav.init();
});

export { AnchorBackNavigation, BackNavigation };