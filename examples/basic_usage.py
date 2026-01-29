#!/usr/bin/env python3
"""
Example usage of resume-parser library.

Usage:
    python basic_usage.py [args]
"""

import sys
import os

from resume_parser import *


def main():
    """Main example function."""
    print("Example usage of Resume Parser")
    print("="*60)

    # Example 1: Parse a resume from PDF
    print("\n📄 Example 1: Basic Resume Parsing")
    print("-" * 60)
    
    # Replace with your actual PDF path
    pdf_path = "sample_resume.pdf"
    
    try:
        from resume_parser import parse_resume
        
        print(f"Parsing resume: {pdf_path}")
        result = parse_resume(pdf_path)
        
        # Display extracted information
        print("\n✅ Extracted Information:")
        print(f"  Name:     {result.get('name', 'N/A')}")
        print(f"  Role:     {result.get('role', 'N/A')}")
        print(f"  Email:    {result.get('email', 'N/A')}")
        print(f"  Phone:    {result.get('phone', 'N/A')}")
        print(f"  LinkedIn: {result.get('linkedin', 'N/A')}")
        print(f"  Location: {result.get('location', 'N/A')}")
        
        # Display summary
        summary = result.get('summary', '')
        if summary:
            print(f"\n  Summary:\n    {summary[:200]}...")
        
        # Display achievements
        achievements = result.get('achievements', [])
        if achievements:
            print(f"\n  Achievements ({len(achievements)} found):")
            for i, achievement in enumerate(achievements[:3], 1):
                print(f"    {i}. {achievement.get('text', '')[:80]}...")
        
        # Display awards
        awards = result.get('awards', [])
        if awards:
            print(f"\n  Awards ({len(awards)} found):")
            for i, award in enumerate(awards[:3], 1):
                print(f"    {i}. {award.get('text', '')[:80]}...")
                
    except FileNotFoundError:
        print(f"❌ Error: File '{pdf_path}' not found")
        print("\nTo test this example:")
        print("  1. Place a PDF resume in the examples directory")
        print("  2. Update the 'pdf_path' variable with your PDF filename")
        print("  3. Run: python basic_usage.py")
    except Exception as e:
        print(f"❌ Error parsing resume: {e}")
    
    # Example 2: Using individual extraction functions
    print("\n\n📋 Example 2: Individual Extraction Functions")
    print("-" * 60)
    
    sample_text = """
    John Doe
    Senior Software Engineer
    Email: john.doe@example.com
    Phone: +1-555-123-4567
    LinkedIn: linkedin.com/in/johndoe
    Location: San Francisco, CA
    """
    
    from resume_parser import (
        extract_email,
        extract_phone,
        extract_linkedin,
        clean_text
    )
    
    print("\nExtracting from sample text...")
    print(f"  Email:    {extract_email(sample_text)}")
    print(f"  Phone:    {extract_phone(sample_text)}")
    print(f"  LinkedIn: {extract_linkedin(sample_text)}")
    print(f"  Cleaned:  {clean_text(sample_text)[:60]}...")

    print("\n✓ Example complete!")
    print("\nFor more examples, see the documentation:")
    print("https://github.com/rahulbagai/resume-parser#readme")


if __name__ == "__main__":
    main()
