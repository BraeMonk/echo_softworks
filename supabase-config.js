// Fill these in from your Supabase project: Settings → API.
// SUPABASE_ANON_KEY is safe to expose in frontend code — it's the public
// key, and Row Level Security (see supabase/schema.sql) is what actually
// controls who can read/write what. Never put the service_role key here.
window.SUPABASE_URL = 'https://fpjsabdqbxlymqtoemlt.supabase.co';
window.SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZwanNhYmRxYnhseW1xdG9lbWx0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODY5MTI3NzgsImV4cCI6MjEwMjQ4ODc3OH0.C9sIFB64bXYCHmlLYSQTuniEPresBJPFkZrWrLqcKYk';

window.supabaseClient = window.supabase.createClient(
  window.SUPABASE_URL,
  window.SUPABASE_ANON_KEY
);
