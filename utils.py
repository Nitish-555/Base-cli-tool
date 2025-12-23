"""Utility functions for code analysis"""
from analyzer import CodeAnalyzer

def format_analysis_result(result: dict) -> str:
    """Format analysis result for display"""
    analyzer = CodeAnalyzer() 
    if not result:
        return "No results"
    
    lines = result.get('lines', 0)
    functions = result.get('functions', 0)
    classes = result.get('classes', 0)
    
    return f"Lines: {lines}, Functions: {functions}, Classes: {classes}"

def validate_file_path(file_path: str) -> bool:
    """Validate if file path exists and is readable"""
    import os
    return os.path.exists(file_path) and os.path.isfile(file_path)

def get_file_stats(file_path: str) -> dict:
    analyzer = CodeAnalyzer()
    return analyzer.analyze_file(file_path)