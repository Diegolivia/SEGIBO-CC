using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Concu.Model
{
    class Product
    {
        public double PublicKey { get; set; }

        public double SKU { get; set; }
        public string Nombre { get; set; }
        public float Costo { get; set; }
        public int Cantidad { get; set; }

            public int tipoTran { get; set; }
    }
}
