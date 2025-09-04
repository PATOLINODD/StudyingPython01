# Installing


- ### First:
  - You need to create a .venv directory after you clone this repository
  - To achieve this, run the following command: <pre>```python -m venv .venv ```</pre>
  - You can put whatever name you want to the `venv` folder, but since the .gitignore file is ignoring `.venv` folder, I am going to use that name.
- ### Second:
  - Now you have the .venv directory, you need to activate the virtual environment, so any package that you already have on your machine, will not conflict with mine.
  - to activate the virtual environment all you need to do is run the following command: <pre> ```./.venv/Scripts/activate```</pre>
- ### Third
  - Now that you have set those things up, let's move forward to the final command
  - To install all the libraries and dependencies, you just need to run the following command: <pre>```pip install -r requirements.txt```</pre>
  - Now you are ready to use my studies and practice by yourself

## Additional Notes
If for any reason you decide to move this project to another folder, you have to delete the `.venv` folder and create a new one into the folder you just moved the entire project to.
There are no guarantee that your project will run properly if you do not recreate the `.venv` folder. Therefore, the recommendation is to delete that folder and recreate it whenever you moved the project.
