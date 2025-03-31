// Main JavaScript for minimalist portfolio 
document.addEventListener('DOMContentLoaded', function() {
    // Navigation toggle
    const navToggle = document.querySelector('.nav-toggle');
    const nav = document.querySelector('nav');
    
    if (navToggle) {
        navToggle.addEventListener('click', () => {
            nav.classList.toggle('active');
            document.body.classList.toggle('nav-open');
        });
    }
    
    // Close navigation when clicking a link
    document.querySelectorAll('nav a').forEach(link => {
        link.addEventListener('click', () => {
            nav.classList.remove('active');
            document.body.classList.remove('nav-open');
        });
    });
    
    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
        e.preventDefault();
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 50,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Initialize the in-view animation for sections
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
        }
    });
}, observerOptions);

    // Observe all sections for animation
    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });
    
    // Contact reveal functionality
    const contactButtons = document.querySelectorAll('.contact-reveal-btn');
    
    contactButtons.forEach(button => {
        button.addEventListener('click', function() {
            const contactInfo = this.getAttribute('data-contact');
            const contactType = this.getAttribute('data-type');
            const revealSpan = document.getElementById(`${contactType}-revealed`);
            
            // Toggle visibility
            if (revealSpan.classList.contains('visible')) {
                revealSpan.textContent = '';
                revealSpan.classList.remove('visible');
                this.textContent = `Show ${contactType.charAt(0).toUpperCase() + contactType.slice(1)}`;
            } else {
                revealSpan.textContent = contactInfo;
                revealSpan.classList.add('visible');
                this.textContent = `Hide ${contactType.charAt(0).toUpperCase() + contactType.slice(1)}`;
                
                // Create a "Copy" button
                const copyBtn = document.createElement('button');
                copyBtn.textContent = 'Copy';
                copyBtn.classList.add('copy-btn');
                copyBtn.style.marginLeft = '10px';
                copyBtn.style.padding = '2px 8px';
                copyBtn.style.fontSize = '12px';
                copyBtn.style.cursor = 'pointer';
                
                copyBtn.addEventListener('click', function() {
                    navigator.clipboard.writeText(contactInfo).then(() => {
                        const originalText = this.textContent;
                        this.textContent = 'Copied!';
                        setTimeout(() => {
                            this.textContent = originalText;
                        }, 2000);
                    });
                });
                
                revealSpan.appendChild(document.createTextNode(' '));
                revealSpan.appendChild(copyBtn);
            }
        });
    });
    
    // Theme toggle functionality
    const themeToggle = document.querySelector('.theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'dark';
    
    // Apply saved theme
    if (currentTheme) {
        document.body.classList.add(currentTheme + '-theme');
        if (currentTheme === 'dark') {
            document.body.classList.add('bg-dots-light');
        }
    }
    
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const isDark = document.body.classList.contains('dark-theme');
            
            if (isDark) {
                document.body.classList.remove('dark-theme');
                document.body.classList.add('light-theme');
                localStorage.setItem('theme', 'light');
            } else {
                document.body.classList.remove('light-theme');
                document.body.classList.add('dark-theme');
                localStorage.setItem('theme', 'dark');
            }
        });
    }
    
    // Mobile menu toggle
    const menuButton = document.querySelector('.menu-button');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuButton) {
        menuButton.addEventListener('click', () => {
            menuButton.classList.toggle('active');
            navLinks.classList.toggle('show');
        });
    }
    
    // Close mobile menu when a link is clicked
    const navItems = document.querySelectorAll('.nav-links a');
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            if (window.innerWidth <= 768) {
                menuButton.classList.remove('active');
                navLinks.classList.remove('show');
            }
        });
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add enhanced hover effects to project items
    document.querySelectorAll('.project-item').forEach(item => {
        item.addEventListener('mouseenter', function() {
            // Reset transforms for all items
            document.querySelectorAll('.project-item').forEach(otherItem => {
                if (otherItem !== this) {
                    otherItem.style.transform = 'scale(0.95)';
                    otherItem.style.opacity = '0.7';
                }
            });
            
            // Enhance the hovered item
            this.style.transform = 'translateY(-10px) scale(1.03)';
            this.style.zIndex = '10';
        });
        
        item.addEventListener('mouseleave', function() {
            // Reset all items
            document.querySelectorAll('.project-item').forEach(otherItem => {
                otherItem.style.transform = '';
                otherItem.style.opacity = '';
                otherItem.style.zIndex = '';
            });
        });
    });
    
    // Automatically set dark theme as default (already set in HTML)
    localStorage.setItem('theme', 'dark');
    
    // Set dots background as default (already set in HTML)
    localStorage.setItem('background', 'bg-dots-light');
    
    // Add styles for dark/light themes
    const style = document.createElement('style');
    style.textContent = `
        :root[data-theme="light"] {
            --background: #f7f7f7;
            --text: #222;
            --text-secondary: #666;
            --accent: #000;
            --border: #ddd;
        }
        
        :root[data-theme="dark"] {
            --background: #111;
            --text: #f7f7f7;
            --text-secondary: #aaa;
            --accent: #fff;
            --border: #333;
        }
        
        .theme-toggle {
            background: none;
            border: none;
            cursor: pointer;
            font-size: 1.5rem;
            position: fixed;
            top: 1rem;
            left: 1rem;
            z-index: 100;
            mix-blend-mode: difference;
            color: #fff;
        }
        
        section {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        
        section.in-view {
            opacity: 1;
            transform: translateY(0);
        }
        
        .nav-open {
            overflow: hidden;
        }
    `;
    
    document.head.appendChild(style);
}); 