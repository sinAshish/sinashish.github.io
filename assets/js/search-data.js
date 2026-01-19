// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "For up-to-date list. Check my Google Scholar.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-photography",
          title: "photography",
          description: "A collection of moments captured from various places I&#39;ve visited.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/photography/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "My academic CV.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "news-started-as-ml-researcher-at-huawei-noah-s-ark-lab-toronto-tada-man-technologist",
          title: 'Started as ML Researcher at Huawei Noah’s Ark Lab, Toronto :tada: :man_technologist:',
          description: "",
          section: "News",},{id: "news-unpose-is-accepted-to-corl-25-tada-tada",
          title: 'UnPose is accepted to CoRL ‘25 :tada: :tada:',
          description: "",
          section: "News",},{id: "news-starting-as-machine-learning-resident-at-amii-tada-man-technologist",
          title: 'Starting as Machine Learning Resident at Amii :tada: :man_technologist:',
          description: "",
          section: "News",},{id: "projects-project-1",
          title: 'project 1',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
