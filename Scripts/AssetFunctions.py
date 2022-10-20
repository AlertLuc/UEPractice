import unreal
import os


# Create an import resource task
def buildImportTask(filename, destination_path, options=None):
    task = unreal.AssetImportTask()

    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    task.set_editor_property('options', options)
    return task


def buildStaticMeshImportOptions():
    options = unreal.FbxImportUI()

    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', True)
    options.set_editor_property('import_as_skeletal', False)

    options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(50.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 110.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)

    options.static_mesh_import_data.set_editor_property('combine_meshes', True)
    options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
    options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)

    return options


def buildSkeletalMeshImportOptions():
    options = unreal.FbxImportUI()

    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', True)
    options.set_editor_property('import_as_skeletal', True)

    options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 110.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)

    return options


# Animation import Settings options
def buildAnimationImportOptions(skeleton_path):
    options = unreal.FbxImportUI()

    options.set_editor_property('import_animations', True)
    options.skeleton = unreal.load_asset(skeleton_path)

    options.anim_sequence_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.anim_sequence_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.anim_sequence_import_data.set_editor_property('import_uniform_scale', 1.0)

    options.anim_sequence_import_data.set_editor_property('animation_length',
                                                          unreal.FBXAnimationLengthImportType.FBXALIT_EXPORTED_TIME)
    options.anim_sequence_import_data.set_editor_property('remove_redundant_keys', False)
    return options


# Example Import resources
def executeImportTasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            print('Imported: %s' % path)


# Absolute path,not relative path
def importSimpleAssets():
    texture_tga = 'D:/WorkPlace/Scripts/FirstPersonCrosshair.TGA'
    sound_wav = 'D:/WorkPlace/Scripts/FirstPersonTemplateWeaponFire02.WAV'

    texture_task = buildImportTask(texture_tga, '/Game/Texture')
    sound_task = buildImportTask(sound_wav, '/Game/Audio')

    executeImportTasks([texture_task, sound_task])


def importMeshAssets():
    static_mesh_path = 'D:/WorkPlace/Scripts/SM_Chair.FBX'
    skeletal_mesh_path = 'D:/WorkPlace/Scripts/SK_Mannequin.FBX'

    static_mesh_task = buildImportTask(static_mesh_path, '/Game/StaticMeshes', buildStaticMeshImportOptions())
    skeletal_mesh_task = buildImportTask(skeletal_mesh_path, '/Game/SkeletalMeshes', buildSkeletalMeshImportOptions())

    executeImportTasks([static_mesh_task, skeletal_mesh_task])


def importAnimationAssets():
    animation_fbx = "D:/WorkPlace/Scripts/BodyBlock.FBX"
    animation_fbx_task = buildImportTask(animation_fbx, '/Game/Animations',
                                         buildAnimationImportOptions(
                                             '/Game/AnimStarterPack/UE4_Mannequin/Mesh/UE4_Mannequin_Skeleton.UE4_Mannequin_Skeleton'))
    executeImportTasks([animation_fbx_task])


# file saving
def saveAsset(path='', force_save=True):
    return unreal.EditorAssetLibrary.save_asset(asset_to_save=path, only_if_is_dirty=True)


# Save the directory
def saveDirectory(path='', force_save=True, resursive=True):
    return unreal.EditorAssetLibrary.save_directory(directory_path=path, only_if_is_dirty=True,
                                                    recursive=resursive)


# Get a new package
def getPackageFromPath(path):
    return unreal.load_package(path)


# Get all dirty packets
def getAllDirtyPackages():
    packages = []
    for x in unreal.EditorLoadingAndSavingUtils.get_dirty_content_packages():
        packages.append(x)
    for x in unreal.EditorLoadingAndSavingUtils.get_dirty_map_packages():
        packages.append(x)
    return packages


# Save all dirty packets
def saveAllDirtyPackages(show_dialog=False):
    if show_dialog:
        return unreal.EditorLoadingAndSavingUtils.save_dirty_packages_with_dialog(save_map_packages=True,
                                                                                  save_content_packages=True)
    else:
        return unreal.EditorLoadingAndSavingUtils.save_dirty_packages(save_map_packages=True,
                                                                      save_content_packages=True)


# Save the package
def savePackages(packages=None, show_dialog=False):
    if packages is None:
        packages = []
    if show_dialog:
        return unreal.EditorLoadingAndSavingUtils.save_dirty_packages_with_dialog(packages_to_save=packages,
                                                                                  only_dirty=False)
    else:
        return unreal.EditorLoadingAndSavingUtils.save_dirty_packages(packages_to_save=packages,
                                                                      only_dirty=False)


new_dir = '/Game/MyNewDirectory'


# Formal transfer
def importAssets():
    # importSimpleAssets()
    # importMeshAssets()
    importAnimationAssets()

