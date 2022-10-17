import unreal
import os



'''
absolute path,not relative path
'''
texture_tga = 'D:/WorkPlace/FirstPersonCrosshair.TGA' 
sound_wav = 'D:/WorkPlace/FirstPersonTemplateWeaponFire02.WAV' 

'''
Create an import resource task
filename:Create the name of the import
destination_path:Which path to import to UE4
Did not perform
'''
def buildImportTask(filename, destination_path):
	'''
	Create a task object
    Set the properties
    Avoid dialog boxes
    Name
	Path
    Filename
    Whether the override already exists
    Whether or not to save
	'''
	task = unreal.AssetImportTask()
	task.set_editor_property('automated', True)
	task.set_editor_property('destination_name','')
	task.set_editor_property('destination_path', destination_path)
	task.set_editor_property('filename', filename)
	task.set_editor_property('replace_existing', True)
	task.set_editor_property('save', True)
	return task

'''
Example Import resources
The print information
'''
def executeImportTasks(tasks):
	unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
	for task in tasks:
		for path in task.get_editor_property('imported_object_paths'):
			print ('Imported: %s' % path)

'''
Formal transfer
Perform the Create picture task and the audio task
Pass the list in executeImportTasks
'''
def importMyAssets():
	texture_task = buildImportTask(texture_tga, '/FirstPerson/Texture')
	sound_task = buildImportTask(sound_wav, '/FirstPerson/Audio')
	executeImportTasks([texture_task, sound_task])




