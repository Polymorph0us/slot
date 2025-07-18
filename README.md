# Ex03 Time Table
## Date:12.05.2025

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Timetable</title>
    <style>
        table {
            width: 80%;
            border-collapse: collapse;
            margin: 20px auto;
        }
        th, td {
            border: 1px solid #000;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #c5c4e3;
        }
        .header {
            background-color: #f4c2c2;
        }
        .assess {
            background-color: #ffecb3;
        }
        .mentors {
            background-color: #98fb98;
        }
    </style>
</head>
<body>

    <h1 style="text-align:center;"><img src="data:image/png;base64,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"></h1>

    <table>
        <tr class="header">
            <th>Time</th>
            <th>MONDAY</th>
            <th>TUESDAY</th>
            <th>WEDNESDAY</th>
            <th>THURSDAY</th>
            <th>FRIDAY</th>
            <th>SATURDAY</th>
        </tr>
        <tr>
            <td class="assess">8-10</td>
            <td class="assess">ASSESSMENT HOUR</td>
            <td>19MA222-Probability and Queueing Models</td>
            <td>19MA211-Statistics and Numerical Methods</td>
            <td>19EE305-Basic Electrical, Electronics and Measurement Engineering (2 SLOTS)</td>
            <td>19EE309-Programming Microcontrollers</td>
            <td class="assess">ASSESSMENT HOUR</td>
        </tr>
        <tr>
            <td>10-12</td>
            <td>19EY711-Quantitative Ability II</td>
            <td>19EE309-Programming Microcontrollers</td>
            <td>19EE305-Basic Electrical, Electronics and Measurement Engineering (2 SLOTS)</td>
            <td>19EE404-Digital Electronics</td>
            <td>19EY711-Quantitative Ability I</td>
            <td>19EY711-Quantitative Ability I</td>
        </tr>
        <tr>
            <td>1-3</td>
            <td>19MA211-Statistics and Numerical Methods</td>
            <td></td>
            <td class="mentors">MENTORS MEET</td>
            <td>19EY404-Digital Electronics</td>
            <td>19EY711-Quantitative Ability I</td>
            <td>19EY711-Quantitative Ability I</td>
        </tr>
    </table>

</body>
</html>
```

## OUTPUT

![alt text](<Screenshot 2025-05-19 104433.png>)

## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
