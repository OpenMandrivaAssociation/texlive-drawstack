# revision 28582
# category Package
# catalog-ctan /macros/latex/contrib/drawstack
# catalog-date 2012-06-18 14:35:47 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-drawstack
Version:	20120618
Release:	1
Summary:	Draw execution stacks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/drawstack
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drawstack.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drawstack.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This simple LaTeX package provides support for drawing
execution stack (typically to illustrate assembly language
notions). The code is written on top of TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/drawstack/drawstack.sty
%doc %{_texmfdistdir}/doc/latex/drawstack/Makefile
%doc %{_texmfdistdir}/doc/latex/drawstack/README
%doc %{_texmfdistdir}/doc/latex/drawstack/stack-example.pdf
%doc %{_texmfdistdir}/doc/latex/drawstack/stack-example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
