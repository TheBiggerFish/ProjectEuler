Get-ChildItem -Filter "Problem??" -Recurse | Rename-Item -Verbose -NewName{$_.name -replace 'Problem','Problem0' }