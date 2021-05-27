# Django-react-automation

## This is an automation of folder or file structure for django-react integreated projects.<br/>This folder structure is based on the following tutorial<br/> https://youtube.com/playlist?list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j

- This is just an simple version.
- All you have to do is clone the file or repository and run it and also enter your requried project name. 
- Before running the file install the following dependencies.
  - Django
  - npm or Node.js
- After the completion open the package.json file in the frontend folder and replace the code in scripts section with the following code.
```
     "dev": "webpack --mode development --watch",
     "build": "webpack --mode production"
```
- Before developing there are some steps to perform.
  - First create a urls.py file in frontend app or folder and include the path for index file in views.py
  - Second include the frontend.urls file in the urls.py file of your main folder in project
  - Next add the apps to the INSTALLED_APPS section in settings.py file of your main folder as below
  ```
    "frontend.apps.FrontendConfig",
    "api.apps.ApiConfig"
  ```
- **Note** : The apps created are frontend,api so those are added to installed_apps as above.
- To start developing run the following in the main directory
```
  python manage.py
```
- Also to start the npm server change the directory to frontend and run the following code.
```
  npm run dev
```
- For further doubts please refer the tutorial provided above.
