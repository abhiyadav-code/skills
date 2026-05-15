import os
import shutil
from pathlib import Path

def setup_pm_twin():
    # 1. Determine Workspace Root (CWD)
    workspace_root = Path.cwd()
    memory_dir = workspace_root / ".agent" / "memory"
    
    # 2. Create memory directory
    print(f"Creating memory directory at: {memory_dir}")
    memory_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. Define Mappings (Source Template -> Target User File)
    skill_root = Path(__file__).parent.parent
    assets_dir = skill_root / "assets"
    
    files_to_deploy = {
        "context_template.yaml": "pm_context.yaml",
        "glossary_template.md": "glossary.md"
    }
    
    # 4. Deploy Files
    for template_name, target_name in files_to_deploy.items():
        source = assets_dir / template_name
        target = memory_dir / target_name
        
        if not target.exists():
            print(f"Deploying {target_name}...")
            shutil.copy(source, target)
        else:
            print(f"Skipping {target_name} (Already exists)")

    print("\n[SUCCESS] PM Twin Workspace Initialized.")
    print(f"ACTION REQUIRED: Go to {memory_dir} and edit 'pm_context.yaml' with your links.")

if __name__ == "__main__":
    setup_pm_twin()
