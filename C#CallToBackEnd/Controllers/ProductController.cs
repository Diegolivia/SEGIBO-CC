using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;

namespace ConsoleProgram
{
    public class DataObject
    {
        public string Sucursal { get; set; }
        public float SKU { get; set; }
        public String Nombre { get; set; }
        public float Costo { get; set; }
        public float Cantidad{ get; set; }
        public float TipoTransaccion { get; set; }
    }

    public class Class1
    {
        private const string URL = "link"; //123.565.67.4564
        

        static void Main(string[] args)
        {
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri(URL);

          
            client.DefaultRequestHeaders.Accept.Add(
            new MediaTypeWithQualityHeaderValue("application/json"));

          
            HttpResponseMessage response = client.GetAsync("dondelopone").Result;  //api/product o q le sea
            if (response.IsSuccessStatusCode)
            {
                // Parse the response body.
                var dataObjects = response.Content.ReadAsAsync<IEnumerable<DataObject>>().Result;  
                foreach (var d in dataObjects)
                {
                    Console.WriteLine("{0}\t${1}\t{2}\t{3}\t{4}\t{5}\t{6}", d.Sucursal,d.SKU,d.Nombre,d.Costo,d.Cantidad,d.TipoTransaccion);
                }
            }
            else
            {
                Console.WriteLine("{0} ({1})", (int)response.StatusCode, response.ReasonPhrase);
            }

            client.Dispose();
        }
    }
}