#!/usr/bin/env python
# encoding: utf-8
import subprocess
import os
import sys
import djangosettings
from app.models import *

# constants
TEXTILE_DOCUMENT_FILEPATH = "doc.textile"
MARKDOWN_DOCUMENT_FILEPATH = "doc.markdown"
PANDOC_COMMAND = "pandoc"

# avoiding encoding issues
reload(sys)
sys.setdefaultencoding( "utf-8" )

def touch_file(content):
    file = open(TEXTILE_DOCUMENT_FILEPATH, 'w')
    file.write(content)
    file.close()

def read_file():
    file = open(MARKDOWN_DOCUMENT_FILEPATH, 'r')
    new_summary = file.read()
    file.close()
    return new_summary

def delete_file(file):
    os.remove(file)

def erase_temp_files():
    delete_file(TEXTILE_DOCUMENT_FILEPATH)
    delete_file(MARKDOWN_DOCUMENT_FILEPATH)
    
# Convert all wiki pages to markdown
for wikipage in WikiContents.objects.all():
    
    # write wikipage text in textile in temp file
    touch_file(wikipage.text)
    # run pandoc to convert to markdown
    subprocess.call([PANDOC_COMMAND, TEXTILE_DOCUMENT_FILEPATH, "-o", MARKDOWN_DOCUMENT_FILEPATH])
    # read converted result from markdown file
    new_text = read_file()
    
    # update database
    wikipage.text = new_text
    wikipage.save()
    print "updated wikipage ", wikipage.id

# Convert all wiki page history to markdown
for wikipage in WikiContentVersions.objects.all():
    
    # write wikipage text in textile in temp file
    touch_file(wikipage.data)
    # run pandoc to convert to markdown
    subprocess.call([PANDOC_COMMAND, TEXTILE_DOCUMENT_FILEPATH, "-o", MARKDOWN_DOCUMENT_FILEPATH])
    # read converted result from markdown file
    new_text = read_file()
    
    # update database
    wikipage.data = new_text
    wikipage.save()
    print "updated wikipage version ", wikipage.id

# Convert all issues to markdown
for issue in Issues.objects.all():
    
    # write wikipage text in textile in temp file
    touch_file(issue.description)
    # run pandoc to convert to markdown
    subprocess.call([PANDOC_COMMAND, TEXTILE_DOCUMENT_FILEPATH, "-o", MARKDOWN_DOCUMENT_FILEPATH])
    # read converted result from markdown file
    new_text = read_file()
    
    # update database
    issue.description = new_text
    issue.save()
    print "updated issue ", issue.id

# Convert all issue templates to markdown
for issuetemplate in IssueTemplates.objects.all():
    
    # write wikipage text in textile in temp file
    touch_file(issuetemplate.description)
    # run pandoc to convert to markdown
    subprocess.call([PANDOC_COMMAND, TEXTILE_DOCUMENT_FILEPATH, "-o", MARKDOWN_DOCUMENT_FILEPATH])
    # read converted result from markdown file
    new_text = read_file()
    
    # update database
    issuetemplate.description = new_text
    issuetemplate.save()
    print "updated issue template ", issuetemplate.id

# Convert all issue journals to markdown
for issuejournal in IssueJournals.objects.all():
    
    if (issuejournal.notes is None) or (issuejournal.notes == ""):
        continue

    # write wikipage text in textile in temp file
    touch_file(issuejournal.notes)
    # run pandoc to convert to markdown
    subprocess.call([PANDOC_COMMAND, TEXTILE_DOCUMENT_FILEPATH, "-o", MARKDOWN_DOCUMENT_FILEPATH])
    # read converted result from markdown file
    new_text = read_file()
    
    # update database
    issuejournal.notes = new_text
    issuejournal.save()
    print "updated issue journal ", issuejournal.id

# Convert all projects to markdown
for project in Projects.objects.all():
    
    # write wikipage text in textile in temp file
    touch_file(project.description)
    # run pandoc to convert to markdown
    subprocess.call([PANDOC_COMMAND, TEXTILE_DOCUMENT_FILEPATH, "-o", MARKDOWN_DOCUMENT_FILEPATH])
    # read converted result from markdown file
    new_text = read_file()
    
    # update database
    project.description = new_text
    project.save()
    print "updated project ", project.id

erase_temp_files()