from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def get_files(request):
    # Get all the filenames from the data directory
    # and return them as a JSON response
    import os
    from django.conf import settings
    data_dir = os.path.join(settings.BASE_DIR, 'data')
    filenames = os.listdir(data_dir)
    return JsonResponse({'filenames': filenames})

@api_view(['GET']) 
# reto_1 is the name of the function that will be called when the url is called
# it recieves the request as a parameter
# follows this url reto_1/<str:filename>/
def reto_1(request, filename):
    # This function will excecute a bash script
    # that is in the scripts directory
    # and return the output of the script by reading the file in the output directory
    import os
    from django.conf import settings

    print('Filename: ', filename)
    # Get the absolute path of the script
    script_path = os.path.join(settings.BASE_DIR, 'scripts', 'reto1.sh')
    # Get the absolute path of the output directory
    output_dir = os.path.join(settings.BASE_DIR, 'output')
    # Get the absolute path of the data directory
    data_dir = os.path.join(settings.BASE_DIR, 'data')
    # Get the absolute path of the file
    file_path = os.path.join(data_dir, filename)
    # Get the absolute path of the output file
    output_path = os.path.join(output_dir, filename)
    # Execute the script
    os.system(f'bash {script_path} {file_path} {output_path}')
    # Read the output file
    with open(output_path, 'r') as f:
        output = f.read()
    # Create a json object with the output the values are separeted by space
    output = output.split(' ')
    # The first value is the number of words in the file
    output_json = {'words': output[0]}
    # The second value is the full path of the file
    output_json['file_path'] = output[1]

    # Return the output as a JSON response
    return JsonResponse(output_json)


