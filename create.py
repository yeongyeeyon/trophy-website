import os

# Define the directory structure
directories = [
    "my-nextjs-website/public/icons",
    "my-nextjs-website/public/images",
    "my-nextjs-website/src/pages/api",
    "my-nextjs-website/src/pages/collection",
    "my-nextjs-website/src/pages/series",
    "my-nextjs-website/src/components",
    "my-nextjs-website/src/styles",
    "my-nextjs-website/src/utils"
]

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Define the files to create
files = [
    "my-nextjs-website/public/favicon.ico",
    "my-nextjs-website/src/pages/api/catalog.ts",
    "my-nextjs-website/src/pages/index.tsx",
    "my-nextjs-website/src/pages/about-us.tsx",
    "my-nextjs-website/src/pages/testimonial.tsx",
    "my-nextjs-website/src/pages/catalog.tsx",
    "my-nextjs-website/src/pages/collection/[collectionId].tsx",
    "my-nextjs-website/src/pages/series/[seriesId].tsx",
    "my-nextjs-website/src/styles/globals.css",
    "my-nextjs-website/src/styles/Home.module.css",
    "my-nextjs-website/src/utils/db.ts",
    "my-nextjs-website/src/utils/api.ts"
]

# Create the files
for file_path in files:
    with open(file_path, 'w') as file:
        pass

print("Directory structure created successfully.")
