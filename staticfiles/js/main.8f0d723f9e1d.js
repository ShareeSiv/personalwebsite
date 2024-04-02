const colorThemes = {
    theme1: {
      '--text-color': '#fff',
      '--background-color': '#2F2FA2',
      '--nav-color': '#242582',
      '--hover-color': '#F64C72' ,
      '--article-box-color': '#FA8072',
      'icon': 'fa-moon'
    },
    theme2: {
        '--text-color': '#000000',
        '--background-color': '#85DCBA',
        '--nav-color': '#41B3A3',
        '--hover-color': '#E8A87C' ,
        '--article-box-color': '#FA8072',
        'icon': 'fa-sun'
      },
  };

let currentTheme = sessionStorage.getItem('theme') || 'theme1';

applyTheme(currentTheme);

function toggleTheme() {
    currentTheme = currentTheme === 'theme1' ? 'theme2' : 'theme1';
    applyTheme(currentTheme);
    sessionStorage.setItem('theme', currentTheme);
}

function applyTheme(theme) {
    let root = document.documentElement;
    let themeColors = colorThemes[theme];
    for (let key in themeColors) {
        if (key !== 'icon') {
            root.style.setProperty(key, themeColors[key]);
        }
    }
    let iconClass = themeColors['icon'];
    document.getElementById('theme-btn').innerHTML = `<i class="fa-solid ${iconClass}"></i>`;
}