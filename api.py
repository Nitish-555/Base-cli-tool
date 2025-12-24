"""API endpoints for code analysis"""
from analyzer import CodeAnalyzer
from utils import format_analysis_result, validate_file_path

class AnalysisAPI:
    """API for code analysis operations"""
    
    def __init__(self):
        self.analyzer = CodeAnalyzer()
    
    def analyze_endpoint(self, file_path: str) -> dict:
        """API endpoint to analyze a file"""
        if not validate_file_path(file_path):
            return {"error": "Invalid file path"}
        
        result = self.analyzer.analyze_file(file_path)
        formatted = format_analysis_result(result)
        
        return {
            "status": "success",
            "data": result,
            "formatted": formatted
        }
    
    def batch_analyze(self, file_paths: list[str]) -> list[dict]:
        """Analyze multiple files"""
        results = []
        for path in file_paths:
            results.append(self.analyze_endpoint(path))
        return results
    
    def execute_analysis(self, file_path: str, command: str) -> dict:
    """Execute analysis with custom command"""
    import subprocess
    result = subprocess.run(command, shell=True)
    return {"status": result.returncode}