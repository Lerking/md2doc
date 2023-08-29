# Revising module variants.

1. [Open reference document](#open-reference-document)
2. [Update econfig repository](#update-econfig-repository)
3. [Revise module variant](#revise-module-variant)
4. [Check in changes in econfig repository](#check-in-changes-in-econfig-repository)
5. [Import and verify updates in TeamCenter](#import-and-verify-updates-in-teamcenter)
6. [Update models.decanter repository](#update-models-decanter-repository)
7. [Sign off ECN for review](#sign-off-ecn-for-review)
8. [Complete ECN](#complete-ecn)
### Open reference document
Open the reference excel document from TeamCenter.

Check that the MVs to be revised matches the MVs in the Impacted folder.
If there are inconsistencies, contact design engineer to have the reference excel document and/or the Impacted folder updated.

### Update econfig repository
Switch to the ALiCE.econfig.Decanter repository and make sure the __master__ branch is checked out.

Update local files.

### Revise module variant
Either update the MVs directly in TCStudio or using the Excel plugin.

If new domain values are needed, also make sure to add them in eDecanter_domains.tcx

### Check in changes to econfig repository
Once the MVs have been updated, check in the changes in Visual Studio.

Copy the SHA ID for your check in.

### Import and verify updates in Teamcenter
Run the "Import Product Class" workflow.

Once finished, check that new MV revisions have been created in the 'Results' folder and the MVs have all been updated according to the reference excel sheet.

### Update models decanter repository
Check out the Next_release_Dev branch.

Update local files.

Copy updated module file from ALiCE.econfig.Decanter/master branch into ALiCE.models.Decanter/Next_release_Dev branch.
If needed update eDecanter_domains.tcx as well.

Deploy module to ALiCE module files.

### Sign off ECN for review
'Perform' ECN and enter module engineers name for review.
The ECN will now be sent to the module engineers work folder.

### Complete ECN
When review has been done, 'Perform' the ECN and select 'Complete'