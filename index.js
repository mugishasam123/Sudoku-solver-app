import { PythonShell } from "python-shell";

PythonShell.run('./scripts/app.py', null).then(result=>{
    return result
  });

