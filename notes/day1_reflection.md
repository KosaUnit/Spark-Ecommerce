1. What .explain() showed

    a) Parsed Logical Plan - briefle what was written by the user as a code
    b) Analyzed Logical Plan - extend (a) by adding a type to a column and checking if the column exsist 
    c) Optimized Logical Plan - optimize execution plan, remove some filters or add new once, or move operations to avoid what is needed and to reduce calculations 
    d) Physical Plan - based on the optimized plan create exact execution plan with all steps -> like a new code to execute with all best practices enhanced by spark software 

2. What you observed in Spark’s execution

    - in general reading data and filtering it in this case 

3. Anything unclear or surprising

    - I think all is clear 