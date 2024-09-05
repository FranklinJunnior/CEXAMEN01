using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;

var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.MapGet("/", () => "Muchas Peliculas Disponibles");

app.MapGet("/recommend", async (HttpContext context) =>
{
    string? title = context.Request.Query["title"];
    if (string.IsNullOrEmpty(title))
    {
        context.Response.StatusCode = 400;
        await context.Response.WriteAsync("El título de la película no puede estar vacío.");
        return;
    }

    // Dirección de la API Flask en el puerto 5000
    string baseUrl = "http://flask-container:5000";
    using var client = new HttpClient();
    var response = await client.GetAsync($"{baseUrl}/recommend?title={title}");
    response.EnsureSuccessStatusCode();
    var recommendations = await response.Content.ReadFromJsonAsync<string[]>();
    await context.Response.WriteAsJsonAsync(recommendations ?? Array.Empty<string>());
});

app.Run();
