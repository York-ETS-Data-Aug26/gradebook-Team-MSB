## Answers to the Record Prompts

### Stage Four 
`` Abort Merge: PS C:\Users\York Laptop 028\Git_Repos\gradebook-Team-MSB> git merge --abort
fatal: There is no merge to abort (MERGE_HEAD missing). ``
 - Nothing appeared for the git stash and git status --short
 - ae9a8c2 Revert "Breaking the program"
   604214b (origin/branch-B, branch-B) Breaking the program
 -  Example with status:

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   gradebook/storage.py

- Example with diff:

diff --git a/gradebook/storage.py b/gradebook/storage.py
index 06c9377..c07178f 100644
--- a/gradebook/storage.py
+++ b/gradebook/storage.py
@@ -17,4 +17,6 @@ def load(path):
 
 def save(path, roster):
     with open(path, 'w') as file:
-        json.dump(roster, file)
\ No newline at end of file
+        json.dump(roster, file)

End of section four

### Stage Two
- {Mahir and Brandon need to coordinate this}



### Stage Three
-Git did not report and error
-When running main.py we got - “ImportError: cannot import name 'average' from 'gradebook.reports'
(C:\Users\brand\PycharmProjects\gradebook-Team-MSB\gradebook\reports.py)”

-Code fails because C renames average to mean and then is called average in A’s top_student function. 
-Git did not catch it because Git doesn't actually run the code, it just compares the changes.
-One catch could be to review the changes before merging on GitHub. The other could be running main.py before merging.