# File_Converter
Converter XML &lt;-> TXT 

Simply add .txt or .xml file into working directory (where main.py is) and launch main.py program with one argument (file) in terminal.

Application changes .txt file in a followed way:
<li> Single lines are placed into root element -row- </li>
<li> Single words in line are placed into child element -col- </li></br>

f.e sample.txt contains following words:
<ul>London Barcelona Poland(\n)</ul>
<ul>One Two Three(\n)</ul>

As a result of the conversion, the sample.xml file will look as follows:</br>
  <row<</br>
    <col<London</col.></br>
    <col<Barcelona</col.></br>
    <col<Poland</col.></br>
  </row<</br>
  <row<</br>
    <col<One</col.></br>
    <col<Two</col.></br>
    <col<Three</col.></br>
  </row<</br>


