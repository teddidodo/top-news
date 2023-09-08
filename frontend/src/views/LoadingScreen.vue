<template>
    <div class="splash-screen  bg-grey">
      <div class="splash-content">
        <h1>Welcome to My App</h1>
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoadingScreen',
  };
  </script>
  
  <style scoped>
  .splash-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #ffffff; /* Customize the background color */
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .splash-content {
    text-align: center;
    font-size: 24px;
    color: #333; /* Customize the text color */
  }
  
  /* You can add additional styles as needed */
  </style>
  