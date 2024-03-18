def list_guilds(project_id, location_id):
    """Lists all guilds in the given location."""

    client = gaming.GameServiceClient()

    request = gaming.ListGuildsRequest(
        parent=f"projects/{project_id}/locations/{location_id}"
    )

    for guild in client.list_guilds(request=request):
        print(f"Name: {guild.name}")
        print(f"Display name: {guild.display_name}")
        print(f"Description: {guild.description}")
        print(f"Created: {guild.create_time}")
        print(f"Updated: {guild.update_time}")
        guild_names.append(guild.name)

  
