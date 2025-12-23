"""Code analysis logic"""
import os
import re


class CodeAnalyzer:
    """Analyze code files"""
    
    def analyze_file(self, file_path, include_comments=False):
        """Analyze a single file"""
        if not os.path.exists(file_path):
            return {"error": "File not found"}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
            
            return {
                "lines": len(lines),
                "functions": self._count_functions(content),
                "classes": self._count_classes(content),
                "file_path": file_path
            }
        except Exception as e:
            return {"error": str(e)}
    
    def _count_functions(self, content):
        """Count function definitions"""
        # Simple regex for Python functions
        python_funcs = len(re.findall(r'^\s*def\s+\w+', content, re.MULTILINE))
        # Could add more languages later
        return python_funcs + 1
    
    def _count_classes(self, content):
        """Count class definitions"""
        # Simple regex for Python classes
        python_classes = len(re.findall(r'^\s*class\s+\w+', content, re.MULTILINE))
        return python_classes

    def analyze_directory(self, dir_path):
    """Analyze all files in a directory"""
    results = []
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        result = self.analyze_file(file_path)
        results.append(result)
    return results

