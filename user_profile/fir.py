def state_detail(request):
    if request.method == 'POST':
        state_name = request.POST.get('state_name')
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        num_people = request.POST.get('num_people')
        companions = request.POST.get('companions')

        # Convert date strings to datetime objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        # Calculate number of days between start date and end date
        num_days = (end_date - start_date).days

        if state_name in datavalue:
            state_data = datavalue[state_name]

            # Filter places based on number of days
            if num_days:
                state_data = [place for place in state_data if 'type' in place and place['type'] != 'Entertainment']
                random.shuffle(state_data)  # Shuffle the list randomly
                state_data = state_data[:int(num_days)]

            # Create a list of tuples with the longitude and latitude values for each place
            coordinates = [(place['long'], place['lat']) for place in state_data]

            # Create a folium map object
            my_map = folium.Map(location=[38.8949549, -77.0366456], zoom_start=10)

            # Add markers to the map for each coordinate
            # Add markers to the map for each coordinate
            for place in state_data:
                coordinate = (place['long'], place['lat'])
                place_name = place['place']
                folium.Marker(location=coordinate, popup=place_name).add_to(my_map)

            # Convert the map object to HTML
            map_html = my_map._repr_html_()

            # Pass the map HTML to the context dictionary and render the template
            context = {'state_data': state_data, 'map_html': map_html}
            return render(request, 'home2/state_details.html', context)

        else:
            error_msg = 'Sorry, we do not have any information for the state you entered.'
            context = {'error_msg': error_msg}
            return render(request, 'home2/state_details.html', context)
    else:
        return render(request, 'home2/state_details.html')


